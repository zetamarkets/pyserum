"""Test instructions."""

from solders.pubkey import Pubkey

import pyserum.instructions as inlib
from pyserum.enums import OrderType, Side


def test_initialize_market():
    """Test initialize market."""
    params = inlib.InitializeMarketParams(
        market=Pubkey(0),
        request_queue=Pubkey(1),
        event_queue=Pubkey(2),
        bids=Pubkey(3),
        asks=Pubkey(4),
        base_vault=Pubkey(5),
        quote_vault=Pubkey(6),
        base_mint=Pubkey(7),
        quote_mint=Pubkey(8),
        base_lot_size=1,
        quote_lot_size=2,
        fee_rate_bps=3,
        vault_signer_nonce=4,
        quote_dust_threshold=5,
    )
    instruction = inlib.initialize_market(params)
    assert inlib.decode_initialize_market(instruction) == params


def test_new_orders():
    """Test match orders."""
    params = inlib.NewOrderParams(
        market=Pubkey(0),
        open_orders=Pubkey(1),
        payer=Pubkey(2),
        owner=Pubkey(3),
        request_queue=Pubkey(4),
        base_vault=Pubkey(5),
        quote_vault=Pubkey(6),
        side=Side.BUY,
        limit_price=1,
        max_quantity=1,
        order_type=OrderType.IOC,
        client_id=1,
    )
    instruction = inlib.new_order(params)
    assert inlib.decode_new_order(instruction) == params


def test_match_orders():
    """Test match orders."""
    params = inlib.MatchOrdersParams(
        market=Pubkey(0),
        request_queue=Pubkey(1),
        event_queue=Pubkey(2),
        bids=Pubkey(3),
        asks=Pubkey(4),
        base_vault=Pubkey(5),
        quote_vault=Pubkey(6),
        limit=1,
    )
    instruction = inlib.match_orders(params)
    assert inlib.decode_match_orders(instruction) == params


def test_consume_events():
    params = inlib.ConsumeEventsParams(
        market=Pubkey(0),
        event_queue=Pubkey(1),
        open_orders_accounts=[Pubkey(i + 2) for i in range(8)],
        limit=1,
    )
    instruction = inlib.consume_events(params)
    assert inlib.decode_consume_events(instruction) == params


def test_cancel_order():
    """Test cancel order."""
    params = inlib.CancelOrderParams(
        market=Pubkey(0),
        request_queue=Pubkey(1),
        owner=Pubkey(2),
        open_orders=Pubkey(3),
        side=Side.BUY,
        order_id=1,
        open_orders_slot=1,
    )
    instruction = inlib.cancel_order(params)
    assert inlib.decode_cancel_order(instruction) == params


def test_cancel_order_by_client_id():
    """Test cancel order by client id."""
    params = inlib.CancelOrderByClientIDParams(
        market=Pubkey(0), request_queue=Pubkey(1), owner=Pubkey(2), open_orders=Pubkey(3), client_id=1
    )
    instruction = inlib.cancel_order_by_client_id(params)
    assert inlib.decode_cancel_order_by_client_id(instruction) == params


def test_settle_funds():
    """Test settle funds."""
    params = inlib.SettleFundsParams(
        market=Pubkey(0),
        owner=Pubkey(1),
        open_orders=Pubkey(2),
        base_vault=Pubkey(3),
        quote_vault=Pubkey(4),
        base_wallet=Pubkey(5),
        quote_wallet=Pubkey(6),
        vault_signer=Pubkey(7),
    )
    instruction = inlib.settle_funds(params)
    assert inlib.decode_settle_funds(instruction) == params


def test_close_open_orders():
    """Test settle funds."""
    params = inlib.CloseOpenOrdersParams(
        open_orders=Pubkey(0),
        owner=Pubkey(1),
        sol_wallet=Pubkey(2),
        market=Pubkey(3),
    )
    instruction = inlib.close_open_orders(params)
    assert inlib.decode_close_open_orders(instruction) == params


def test_init_open_orders():
    """Test settle funds."""
    params = inlib.InitOpenOrdersParams(open_orders=Pubkey(0), owner=Pubkey(1), market=Pubkey(2), market_authority=None)
    instruction = inlib.init_open_orders(params)
    assert inlib.decode_init_open_orders(instruction) == params


def test_init_open_orders_with_authority():
    """Test settle funds."""
    params = inlib.InitOpenOrdersParams(
        open_orders=Pubkey(0),
        owner=Pubkey(1),
        market=Pubkey(2),
        market_authority=Pubkey(3),
    )
    instruction = inlib.init_open_orders(params)
    assert inlib.decode_init_open_orders(instruction) == params
