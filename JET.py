import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# implement class for Journal Entry Tests (JET)
class JET:
    def __init__(self) -> None:
        pass

    def __version__(self) -> str:
        return "0.0.1"

    def get_data(self, data: pd.DataFrame) -> None:
        self.data = data

    def reconciliation_line_item_control_totals(
        self, name_col: str, name_debit_col: str, name_credit_col: str
    ) -> pd.DataFrame:
        # get control totals
        control_totals = self.data.groupby(name_col).agg(
            {name_debit_col: "sum", name_credit_col: "sum"}
        )
        control_totals = control_totals.reset_index()
        control_totals = control_totals.rename(
            columns={name_debit_col: "debit", name_credit_col: "credit"}
        )
        control_totals["balance"] = control_totals["debit"] - control_totals["credit"]
        return control_totals

    def reconciliation_line_item_control_totals_plot(
        self, name_col: str, name_debit_col: str, name_credit_col: str
    ) -> go.Figure:
        # get control totals
        control_totals = self.reconciliation_line_item_control_totals(
            name_col, name_debit_col, name_credit_col
        )
        # plot
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Debit", "Credit"))
        fig.add_trace(
            go.Bar(x=control_totals[name_col], y=control_totals["debit"], name="debit"),
            row=1,
            col=1,
        )
        fig.add_trace(
            go.Bar(
                x=control_totals[name_col], y=control_totals["credit"], name="credit"
            ),
            row=1,
            col=2,
        )
        fig.update_layout(title_text="Reconciliation Line Item Control Totals")
        return fig

    def je_not_balance_to_zero(self, name_debit, name_credit) -> pd.DataFrame:
        # get journal entries that do not balance to zero
        not_balance_to_zero = self.data[
            self.data[name_debit] - self.data[name_credit] != 0
        ]
        return not_balance_to_zero

    def je_not_balance_to_zero_plot(self, name_debit, name_credit) -> go.Figure:
        # get journal entries that do not balance to zero
        not_balance_to_zero = self.je_not_balance_to_zero(name_debit, name_credit)
        # plot
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Debit", "Credit"))
        fig.add_trace(
            go.Bar(
                x=not_balance_to_zero[name_debit],
                y=not_balance_to_zero[name_debit],
                name="debit",
            ),
            row=1,
            col=1,
        )
        fig.add_trace(
            go.Bar(
                x=not_balance_to_zero[name_credit],
                y=not_balance_to_zero[name_credit],
                name="credit",
            ),
            row=1,
            col=2,
        )
        fig.update_layout(title_text="Journal Entries that do not Balance to Zero")
        return fig
