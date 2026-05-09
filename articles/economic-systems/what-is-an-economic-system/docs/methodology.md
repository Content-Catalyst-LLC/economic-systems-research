# Methodology

## Purpose

This article companion provides a reproducible framework for representing an economic system as a structured set of sectors, institutions, allocation choices, distributional outcomes, and reproduction constraints.

The workflow:

1. Creates a small synthetic multi-sector economy.
2. Defines an inter-industry requirements matrix.
3. Solves the Leontief input-output system.
4. Runs final-demand shock scenarios.
5. Constructs an allocation identity across consumption, investment, public provision, and restoration.
6. Computes distribution metrics, including wage-share and simple inequality summaries.
7. Simulates produced-capital and ecological reproduction constraints.
8. Exports tables, figures, and a SQLite database.
9. Replicates the same logic across Python, R, Stata, SQL, and Julia.

## Core Concepts

- Economic systems are institutional structures, not merely markets.
- Input-output analysis shows sectoral interdependence.
- Allocation identities show that output must be distributed across competing social purposes.
- Distribution metrics reveal how gains and risks are shared.
- Reproduction constraints show whether systems maintain the conditions of future production.
- Ecological foundations are not external to economic life; they are preconditions of production.

## Limitations

The workflow uses a stylized synthetic dataset for teaching and article support. It is not a calibrated national input-output table or a full social accounting matrix. It is designed to make the article's conceptual claims computationally inspectable.
