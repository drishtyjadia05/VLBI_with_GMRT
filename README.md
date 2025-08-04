# Experimental VLBI using NCRA 15m Antenna, GMRT, and ORT

**Author**: Drishty B. Jadia  
**Institution**: IIT Kanpur  
**Host Institute**: National Centre for Radio Astrophysics ([NCRA-TIFR](http://www.ncra.tifr.res.in/ncra/main)), Pune  
**Mentor**: [Dr. Visweshwar Ram Marthi](http://www.ncra.tifr.res.in/~viswesh/)  
**Program**: Visiting Students’ Research Program (VSRP) 2024  

---

## Abstract

This project explores the feasibility of conducting Very Long Baseline Interferometry (VLBI) using Indian radio telescopes on intermediate and long baselines. Observations were carried out using the **NCRA 15m antenna**, the **Giant Metrewave Radio Telescope (GMRT)**, and the **Ooty Radio Telescope (ORT)** at L-band (1.4 GHz) and 325 MHz. The baselines tested span ~80 km (15m–GMRT) and ~1000 km (ORT–GMRT), yielding angular resolutions of ~0.6″ and ~0.25″ respectively—significantly finer than GMRT's native resolution.

The project involved detailed assessment of clock synchronization, reference standard stability, pulsar-based timing validation, and offline correlation for fringe detection. While interferometric fringes could not be detected for the GMRT–15m baseline due to timestamping issues, **successful VLBI fringes were detected between GMRT and ORT**, confirming the feasibility of long-baseline VLBI within India.

---

## Objectives

- Evaluate the phase and frequency stability of OCXO (15m) against hydrogen maser references (GMRT, ORT).
- Estimate baseline sensitivity and required integration times using radiometric calculations.
- Perform pulsar-based delay calibration and timestamp verification.
- Attempt offline fringe detection for two baselines: GMRT–15m and GMRT–ORT.
- Identify practical limitations and provide recommendations for future VLBI operations using Indian telescopes.

---

## Methods

### Frequency Standard Stability

- Conducted a controlled lab experiment using **ROACH boards** and a broadband noise source to compare **OCXO vs Maser** performance.
- Phase stability analyzed using FFTs and cross-correlations on two-hour long datasets.
- Measured delay drift (~17 ns/hr) and frequency drift (~4 µHz/MHz), confirming OCXO suitability for short integrations (~minutes).

### Delay Estimation and Pulsar Timing

- Simultaneous observations of calibrators and pulsars were conducted:
  - GMRT–15m: 3C147 and PSR B0329+54
  - GMRT–ORT: 3C286 and PSR B0950+08
- Delay estimated by aligning pulsar pulse trains and cross-correlating voltage streams.
- Pulse trains were dedispersed and compared sample-by-sample to verify timestamp alignment.

### Offline Fringe Detection

- GMRT–15m: Delay peak found, but no clear fringe due to unsynchronized 1PPS trigger and unknown electronics delay at 15m.
- GMRT–ORT: Fringes successfully detected via offline correlation in Japan. Fringe amplitude and cross-spectrum confirmed broadband coherence.

---

## Tools and Technologies

| Category         | Tools Used                                 |
|------------------|---------------------------------------------|
| Data Acquisition | ROACH boards, Noise generators              |
| Software         | Python, NumPy, Matplotlib, FFT libraries    |
| Telescopes       | GMRT, NCRA 15m, ORT                         |
| Signal Analysis  | Custom scripts for delay/fringe estimation  |
| VLBI Correlation | Offline correlator (external collaboration) |

---

## Key Findings

- **OCXO-based timing** is feasible for VLBI with short integration times, though inferior to H-masers in long-term phase stability.
- Pulsar timing validated sub-sample level synchronization between ORT and GMRT.
- First-ever experimental detection of VLBI fringe on the GMRT–ORT baseline with Indian telescopes at 325 MHz.
- Identified critical bottlenecks: timestamping at 15m, electronics delay calibration, and broader delay smearing effects.

---

## Repository Contents

- `/plots/` — Figures showing delay rates, Doppler shifts, pulse trains, and fringes.
- `/scripts/` — Python scripts for delay estimation and cross-correlation.
- `/report/` — [Full Technical Report (PDF)](./VSRP_REPORT.pdf)
- `/data/` — Placeholder for processed visibility data and example baseband segments (*optional*).

---

## Contact

Drishty B. Jadia  
Email: dbjadia05@gmail.com  
