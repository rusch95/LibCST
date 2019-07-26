# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict
from typing import Any

import libcst as cst
from libcst._nodes._internal import CodeRange
from libcst._nodes.tests.base import CSTNodeTest
from libcst.testing.utils import data_provider


class ElseTest(CSTNodeTest):
    @data_provider(
        (
            {
                "node": cst.Else(cst.SimpleStatementSuite((cst.Pass(),))),
                "code": "else: pass\n",
                "expected_position": CodeRange.create((1, 0), (1, 10)),
            },
            {
                "node": cst.Else(
                    cst.SimpleStatementSuite((cst.Pass(),)),
                    whitespace_before_colon=cst.SimpleWhitespace("  "),
                ),
                "code": "else  : pass\n",
                "expected_position": CodeRange.create((1, 0), (1, 12)),
            },
        )
    )
    def test_valid(self, **kwargs: Any) -> None:
        self.validate_node(**kwargs)
