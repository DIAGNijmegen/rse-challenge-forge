from contextlib import nullcontext

import pytest

from challenge_forge.exceptions import InvalidContextError
from challenge_forge.forge import generate_challenge_pack
from tests.utils import pack_context_factory


@pytest.mark.parametrize(
    "json_context,condition",
    [
        [{}, pytest.raises(InvalidContextError)],
        ["", pytest.raises(InvalidContextError)],
        [{"challenge": []}, pytest.raises(InvalidContextError)],
        [{}, pytest.raises(InvalidContextError)],
        [
            {"challenge": {}},
            pytest.raises(InvalidContextError),
        ],
        [
            pack_context_factory(),
            nullcontext(),
        ],
        [
            pack_context_factory({"challenge": {"phases": []}}),
            nullcontext(),
        ],
    ],
)
def test_fails(json_context, condition, tmp_path):
    with condition:
        generate_challenge_pack(
            context=json_context, output_directory=tmp_path
        )
