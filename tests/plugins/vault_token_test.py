import pytest

from detect_secrets.plugins.vault_token import VaultTokenDetector


class TestVaultTokenDetector:

    @pytest.mark.parametrize(
        'payload, should_flag',
        [
            ('hvs.s7w8JQkX9gZm2qL3yA0oYbVnTrPc5e-U', True),
            ('hvs.ABCD1234efgh5678ijklMNOPqrst_uv', True),
            ('hvs.Zyxwvu9876543210tsrqponmlkjihgf-', True),
            ('hvb.98asdhAHSd8237hads_asd8123-asd1', True),
            ('hvb.MNOPqrstUVWXyz0123456789_abcdEF', True),
            ('hvb.abcdEFGHijklMNOP1234567890-_Qrs', True),
            ('hvz.1234567890abcdef', False),
            ('hvs-1234567890abcdef', False),
            ('hvb_abcdefghijklmno', False),
            ('abcdefghijklmnopqrstuvwxyz123456', False),
            ('token-hvs-1234567890abcdef', False),
            
        ],
    )
    def test_analyze_line(self, payload, should_flag):
        logic = VaultTokenDetector()

        output = logic.analyze_line(filename='mock_filename', line=payload)
        assert len(output) == int(should_flag)
