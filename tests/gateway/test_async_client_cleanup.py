import pytest
from unittest.mock import patch


def test_gateway_async_client_cleanup_calls_stale_cleanup_by_default():
    from gateway.run import _cleanup_gateway_async_clients

    with patch("agent.auxiliary_client.cleanup_stale_async_clients") as cleanup, patch(
        "agent.auxiliary_client.shutdown_cached_clients"
    ) as shutdown:
        _cleanup_gateway_async_clients()

    cleanup.assert_called_once()
    shutdown.assert_not_called()


def test_gateway_async_client_cleanup_can_shutdown_all_cached_clients():
    from gateway.run import _cleanup_gateway_async_clients

    with patch("agent.auxiliary_client.cleanup_stale_async_clients") as cleanup, patch(
        "agent.auxiliary_client.shutdown_cached_clients"
    ) as shutdown:
        _cleanup_gateway_async_clients(final=True)

    cleanup.assert_called_once()
    shutdown.assert_called_once()
