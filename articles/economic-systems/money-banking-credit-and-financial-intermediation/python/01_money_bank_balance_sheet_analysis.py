"""
Money aggregates, bank balance sheets, deposit creation, leverage, and debt-service capacity.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
FIGURE_DIR = BASE_DIR / "outputs" / "figures"
TABLE_DIR = BASE_DIR / "outputs" / "tables"

for directory in [FIGURE_DIR, TABLE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


def main() -> None:
    money = pd.read_csv(PROCESSED_DIR / "money_aggregate_scenarios.csv")
    banks = pd.read_csv(PROCESSED_DIR / "bank_balance_sheet_scenarios.csv")
    debt = pd.read_csv(PROCESSED_DIR / "debt_service_scenarios.csv")

    money["money_supply"] = money["currency"] + money["deposits"]
    money["broad_liquidity_proxy"] = money["money_supply"] + money["near_money_claims"]
    money["deposit_share_of_money"] = money["deposits"] / money["money_supply"]
    money.to_csv(TABLE_DIR / "money_aggregate_results_python.csv", index=False)

    banks["leverage"] = banks["assets"] / banks["equity"]
    banks["capital_ratio"] = banks["equity"] / banks["assets"]
    banks["loan_to_deposit_ratio"] = banks["loans"] / banks["bank_deposits"]
    banks["liquid_asset_ratio"] = banks["liquid_assets"] / banks["assets"]
    banks["wholesale_funding_share"] = banks["wholesale_funding"] / banks["assets"]
    banks.to_csv(TABLE_DIR / "bank_balance_sheet_results_python.csv", index=False)

    new_loan = 75
    deposit_creation = banks[["bank", "assets", "bank_deposits", "equity"]].copy()
    deposit_creation["new_loan"] = new_loan
    deposit_creation["assets_after"] = deposit_creation["assets"] + new_loan
    deposit_creation["deposits_after"] = deposit_creation["bank_deposits"] + new_loan
    deposit_creation["leverage_after"] = deposit_creation["assets_after"] / deposit_creation["equity"]
    deposit_creation.to_csv(TABLE_DIR / "deposit_creation_results_python.csv", index=False)

    debt["interest_coverage_ratio"] = debt["income_or_ebit"] / debt["interest_payment"]
    debt["debt_service_ratio"] = (debt["interest_payment"] + debt["principal_payment"]) / debt["income_or_ebit"]
    debt["stressed_interest_payment"] = debt["interest_payment"] * (1 + debt["rate_shock_bps"] / 10000 * 4)
    debt["stressed_interest_coverage_ratio"] = debt["income_or_ebit"] / debt["stressed_interest_payment"]
    debt["stressed_debt_service_ratio"] = (debt["stressed_interest_payment"] + debt["principal_payment"]) / debt["income_or_ebit"]
    debt["debt_stress_flag"] = (debt["stressed_debt_service_ratio"] > 0.40).astype(int)
    debt.to_csv(TABLE_DIR / "debt_service_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(banks["bank"], banks["leverage"])
    ax.set_title("Bank Leverage by Institution")
    ax.set_ylabel("Assets / equity")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "bank_balance_sheet_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(deposit_creation["bank"], deposit_creation["leverage_after"] - banks["leverage"])
    ax.set_title("Leverage Change After Stylized Loan Creation")
    ax.set_ylabel("Change in leverage")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "deposit_creation_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(debt["borrower_group"], debt["stressed_debt_service_ratio"])
    ax.axhline(0.40, linestyle="--", label="stress threshold")
    ax.set_title("Debt-Service Burden Under Rate Shock")
    ax.set_ylabel("Stressed debt-service ratio")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "debt_service_python.png", dpi=300)
    plt.close(fig)

    print(money[["scenario", "money_supply", "deposit_share_of_money"]])
    print(banks[["bank", "leverage", "loan_to_deposit_ratio", "liquid_asset_ratio"]])
    print(debt[["borrower_group", "stressed_debt_service_ratio", "debt_stress_flag"]])


if __name__ == "__main__":
    main()
