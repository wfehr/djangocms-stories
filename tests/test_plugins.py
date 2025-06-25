def test_blog_latest_entries_plugin(admin_client, simple_w_placeholder, assert_html_in_response):
    from cms import api
    from cms.models import Placeholder
    from cms.toolbar.utils import get_object_preview_url
    from .factories import PostContentFactory

    page = api.create_page(
        title="Test Page",
        template="base.html",
        language="en",
    )
    page_content = page.get_admin_content("en")
    placeholder = Placeholder.objects.create(slot="content", source=page_content)
    api.add_plugin(
        placeholder,
        "BlogLatestEntriesPlugin",
        "en",
    )
    url = get_object_preview_url(page_content)

    response = admin_client.get(url, follow=True)
    assert_html_in_response('<p class="blog-empty">No article found.</p>', response)

    batch = PostContentFactory.create_batch(5, language="en", post__app_config=simple_w_placeholder)
    response = admin_client.get(url, follow=True)
    for post_content in batch:
        assert_html_in_response(
            post_content.title,
            response,
        )
        assert_html_in_response(
            post_content.abstract,
            response,
        )


def xtest_author_post_list_plugin(admin_client, simple_w_placeholder, assert_html_in_response):
    from cms import api
    from cms.models import Placeholder
    from cms.toolbar.utils import get_object_preview_url
    from .factories import PostContentFactory

    batch = PostContentFactory.create_batch(5, language="en", post__app_config=simple_w_placeholder)
    authors = [batch[0].author, batch[1].author]

    page = api.create_page(
        title="Test Page",
        template="base.html",
        language="en",
    )
    page_content = page.get_admin_content("en")
    placeholder = Placeholder.objects.create(slot="content", source=page_content)
    plugin = api.add_plugin(
        placeholder,
        "BlogAuthorPostsListPlugin",
        "en",
    )
    instance = plugin.get_plugin_instance()[0]
    instance.authors.add(batch[0].author)
    instance.authors.add(batch[1].author)

    url = get_object_preview_url(page_content)

    response = admin_client.get(url)
    assert_html_in_response(
        f"<h3>Articles by {authors[0].get_full_name()}</h3>",
        response,
    )
    assert_html_in_response(
        authors[1].get_full_name(),
        response,
    )
