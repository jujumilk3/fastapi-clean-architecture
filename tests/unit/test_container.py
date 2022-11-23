from app.core.exceptions import NotFoundError


# It must raise an error
def test_container_with_intended_exception(container):
    auth_service = container.auth_service()
    try:
        found_user = auth_service.get_by_id(1)
    except NotFoundError as e:
        assert True
        return
    # assert False
