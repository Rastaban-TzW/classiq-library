from tests.utils_for_testbook import (
    validate_quantum_program_size,
    validate_quantum_model,
    wrap_testbook,
)
from testbook.client import TestbookNotebookClient


@wrap_testbook("option_pricing", timeout_seconds=140)
def test_notebook(tb: TestbookNotebookClient) -> None:
    # test models
    validate_quantum_model(tb.ref("qmod"))
    # test quantum programs
    validate_quantum_program_size(
        tb.ref("qprog"),
        expected_width=10,  # actual width: 8
        expected_depth=9500,  # actual depth: 8934
    )

    # test notebook content
    assert tb.ref(
        "np.isclose(measured_payoff,expected_payoff,atol=10 * (confidence_interval[1] - confidence_interval[0]))"
    )
