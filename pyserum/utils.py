from solders.pubkey import Pubkey
from solana.rpc.api import Client
from solders.rpc.responses import RPCResult
from spl.token.constants import WRAPPED_SOL_MINT

from pyserum._layouts.market import MINT_LAYOUT


def parse_bytes_data(res: RPCResult) -> bytes:
    if not hasattr(res, "value"):
        raise Exception("Cannot load byte data.")
    data = res.value.data
    return data


def load_bytes_data(addr: Pubkey, conn: Client) -> bytes:
    res = conn.get_account_info(addr)
    return parse_bytes_data(res)


def parse_mint_decimals(bytes_data: bytes) -> int:
    return MINT_LAYOUT.parse(bytes_data).decimals


def get_mint_decimals(conn: Client, mint_pub_key: Pubkey) -> int:
    """Get the mint decimals for a token mint"""
    if mint_pub_key == WRAPPED_SOL_MINT:
        return 9

    bytes_data = load_bytes_data(mint_pub_key, conn)
    return parse_mint_decimals(bytes_data)
