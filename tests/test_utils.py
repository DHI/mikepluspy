from pathlib import Path

import pytest

from mikeplus.utils import _try_setup_default_bin_path


def test_no_default_install_root_names_env_var():
    with pytest.raises(FileNotFoundError, match="MIKEPLUSPY_INSTALL_ROOT"):
        _try_setup_default_bin_path(None, Path("bin/x64"), "MIKEPLUSPY_INSTALL_ROOT")
