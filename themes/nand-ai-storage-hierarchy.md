---
type: theme
name: nand-ai-storage-hierarchy
tickers: [NVDA, SNDK, 000660-KS]
updated: 2026-10-07
data_through: GTC 2026 announcements; HBF status as of Oct 2026
status: imported
sources: [chat:https://claude.ai/chat/3e6404a5-c21b-4892-b92b-622d416f1d55]
---

# NAND in the AI rack — in-rack vs external NAND, and high-bandwidth flash (2026-10-07)

Companies covered: [[NVDA]] (Vera Rubin NVL72, BlueField-4, CMX), SanDisk (SNDK), SK hynix (000660.KS), VAST Data (private). No hubs yet except NVDA. Related: [[ai-infrastructure-cycle]].

> **Imported** on 2026-11-26 from the Global Tech Project chat "In-rack NAND and GPU storage" (2026-10-07). Claude's replies are copied as written, with tool calls removed; Paul's questions are kept as the section headings. Explanatory notes, not an investment view. **Claude's framing, not Paul's view.**

## 1. "I am learning about the in-rack NAND content vs the external NAND. Can you help me understand what the in-rack NAND is for? Why do we need NAND close to the GPUs?"

**Short answer:** in-rack NAND is the rung of the memory ladder between the DRAM on the compute tray and the networked storage arrays. GPUs are the most expensive thing in the building, and any time they wait on data is wasted. NAND inside the rack is the cheapest capacity that can still feed a GPU in microseconds without crossing the network. The reason it's suddenly a big line item is inference, not training.

**What it physically is**

On a Vera Rubin NVL72 compute tray, there are four E1.S Gen6 NVMe bays plus one Gen5 boot drive, alongside the BlueField-4 DPU; with 18 trays that's ~72 data SSDs per rack, each sitting on PCIe next to four GPUs. On top of that, Nvidia has added a second in-rack/in-pod layer: the BlueField-4 STX reference architecture announced at GTC 2026, whose first rack-scale implementation is the CMX context memory storage platform. "External NAND" is the separate storage racks (VAST, DDN, WEKA, Pure, hyperscaler in-house) reached over the Ethernet/InfiniBand fabric.

**The ladder**

Per VR200 rack: 20.7 TB HBM4 plus 54 TB LPDDR5X, then hundreds of TB of local NVMe, then petabytes external. Each rung is roughly 10x cheaper per bit and 10x slower. In-rack NAND exists because the gap between "DRAM is full" and "go to the network" is too expensive to leave empty.

**What it's used for**

1. *KV cache / context memory* — the new driver. Every token in a model's context produces key/value tensors that must be kept for each subsequent generation step. Context windows are now hundreds of thousands of tokens, so the KV cache outgrows HBM; the fallback is offloading to host DRAM or NVMe, but both paths traditionally run through the CPU, adding latency that compounds with context length. For agentic workloads the context has to persist between turns and across agents, so the choice is either recompute it (burn GPU time on prefill) or park it somewhere cheap and fast. Nvidia frames CMX as a "G3.5" tier of pod-level context memory, with NVMe key-value extensions matching how inference frameworks manage KV blocks. Nvidia claims up to 5x tokens per second and 5x better power efficiency versus traditional storage.
2. *Training* — absorbing checkpoint write bursts locally before draining to external storage, and caching shuffled training data so GPUs don't stall on the network.
3. *Model weight loading* — fast swaps for multi-model serving.
4. Boot, OS, logs — trivial in volume.

**Why close rather than external**

- Latency and path: BlueField-4 manages the NVMe SSDs directly and handles integrity and encryption, so context stays accessible at the storage processor rather than transiting the host.
- Bandwidth scales with the rack: every tray brings its own PCIe lanes, whereas external arrays bottleneck on NICs and switch ports shared by many racks.
- It keeps the scale-out fabric for GPU-to-GPU collectives rather than storage traffic.

**Why external storage still exists**

In-rack NAND is per node, limited in capacity, and not a shared namespace. Datasets, model repositories and long-term checkpoints stay external. The interesting development is that the boundary is blurring: VAST runs its software natively on the BlueField-4 DPUs to give each host a shared, coherent context namespace over RDMA, so the "in-rack" tier is becoming a pod-level shared tier rather than strictly local.

**For your NAND work**

- Content per rack is rising fast: Morgan Stanley reportedly expects a VR200 NVL72 rack at ~$7.8m, with ~$2m memory-related and roughly $1m or more in storage, versus NAND being far less central in earlier racks.
- The two tiers buy different products. In-rack is performance TLC, PCIe Gen5/6, E1.S form factor, and endurance matters because KV cache is write-heavy and ephemeral. External is high-capacity QLC (60–120TB+ drives). Different suppliers win in each.
- The next step on the ladder is NAND on the GPU package itself (SanDisk's high-bandwidth flash, targeted at 2027), which would compete with the DRAM rung, not the storage one.

Sources:
- [Nvidia launches BlueField-4 STX at GTC 2026 (Tom's Hardware)](https://tomshardware.com/tech-industry/nvidia-launches-bluefield-4-stx-storage-architecture-for-agentic-ai)
- [Nvidia press release: BlueField-4 and Inference Context Memory Storage Platform](https://www.nasdaq.com/press-release/nvidia-bluefield-4-powers-new-class-ai-native-storage-infrastructure-next-frontier-ai)
- [NAND Research note on CMX](https://nand-research.com/research-note-improving-inference-nvidias-inference-context-memory-storage-platform/)
- [Gigabyte Vera Rubin NVL72 rack spec](https://www.gigabyte.com/jp/Enterprise/GIGAPOD-Rack-Scale/AI-DLC-Rack_NVIDIA-Vera-Rubin-NVL72)
- [Cisco/Supermicro Vera Rubin NVL72 data sheet](https://www.cisco.com/site/us/en/solutions/global-partners/supermicro/nvidia-vera-rubin-nvl72-ds.html)
- [VAST Data and Nvidia inference architecture (iTWire)](https://itwire.com/guest-articles/company-news/vast-data-redesigns-ai-inference-architecture-for-the-agentic-era-with-nvidia)
- [Vera Rubin rack cost estimate (Guru3D)](https://guru3d.com/story/nvidia-vera-rubin-ai-rack-cost-reportedly-hits-million/)

## 2. "What does this mean?" (on SanDisk's high-bandwidth flash)

It means NAND is trying to climb one rung higher on the ladder than the SSD slot it occupies today — onto the GPU package itself, next to the HBM.

**What HBF is.** Conceptually, high-bandwidth flash looks and sounds a lot like HBM, but where HBM uses DRAM, HBF uses NAND flash. NAND dies are stacked and sit on the same package as the GPU, talking to it over a wide HBM-style interface, not over PCIe like an SSD. The target is comparable bandwidth to HBM with up to 8–16x the capacity at similar cost. Sandisk and SK hynix signed an MOU to standardise the specification, with first HBF samples targeted for the second half of 2026 and the first AI inference devices using it in early 2027.

**The numbers behind "comparable."** Sandisk's first generation is claimed to reach read bandwidth up to 1.6 TB/s — a bit above HBM3e but well short of HBM4, which is already at 2.5 TB/s per 12-high stack. So it is slower per stack than current HBM but holds an order of magnitude more.

**Why that puts it against DRAM, not SSDs.** Go back to the Vera Rubin rack: 20.7 TB HBM4, 54 TB LPDDR5X, then NVMe. The LPDDR on the Vera CPU exists because HBM is too small and too expensive to hold everything the GPU wants to read quickly, so weights spill over the NVLink-C2C link into CPU memory. HBF is aimed at exactly that job. Because HBM capacity is so limited, mixture-of-experts models have to be spread across many GPUs linked by very fast interconnects; with HBF, even multi-trillion-parameter models could fit in a single accelerator, removing the interconnect bottleneck. That's weights — large, read-constantly, written almost never — which is the data pattern NAND handles well. The intent is to supplement HBM rather than replace it.

The SSD rung does different work: checkpoints, datasets, and the KV-cache tier Nvidia is building around BlueField-4. Those are write-heavy or persistent jobs, and NAND's weakness is write speed and endurance, so HBF isn't designed to take them. An SSD on PCIe and a flash stack on the interposer are not substitutes for each other.

**The caveats.** It's a 2027 product with no announced GPU design win yet; HBF needs far more dies per module than an ordinary flash device, which is a yield and cost question; read latency is still NAND latency, so the software has to hide it; and 8–16x "at similar cost" is a marketing target, not a shipped spec.

**Why it matters for a NAND thesis.** If it works, it's the first time NAND makers sell into the GPU package at HBM-like economics — qualified, custom, high ASP per bit — rather than into commodity enterprise SSDs. The TAM it eats is the LPDDR/HBM-overflow rung, which is why SK hynix, the HBM leader, is co-developing it rather than ignoring it. It does not change the in-rack NVMe story one way or the other.

Sources:
- [Sandisk–SK hynix HBF MOU press release](https://www.businesswire.com/news/home/20250806259749/en/Sandisk-to-Collaborate-with-SK-hynix-to-Drive-Standardization-of-High-Bandwidth-Flash-Memory-Technology)
- [The Register on HBF, July 2026](https://assets.theregister.com/2026/07/30/202619/)

## Evidence log

- 2026-10-07 — Theme note created from the imported chat above (Claude's framing, not Paul's view).
- 2026-11-26 — Imported into the vault from the Global Tech Project.
