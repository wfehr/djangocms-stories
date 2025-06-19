=================
djangocms-stories
=================

|PyPiVersion| |PyVersion| |TestCoverage| |License|

django CMS stieries application - Tell your story in multilingual posts, using the full power of django CMS placeholders.

Supported Django versions:

* Django 4.2

Supported django CMS versions:

* django CMS 5.0+

djangocms-stories is inspired by `Nephila's <https://github.com/nephila>`_ excellent
`djangocms-blog <https://github.com/nephila/djangocms-blog>`_, but has been reimagined
to align with django CMS's new philosophy since version 4: "The design philosophy of
django CMS is to solve something complex with many simple things." This means
djangocms-stories focuses on modularity, simplicity, and seamless integration with the
latest django CMS features, while still providing powerful storytelling capabilities.

************
Installation
************

To install the latest version directly from GitHub, run:

.. code-block:: bash

    pip install git+https://github.com/fsbraun/djangocms-stories.git

Add ``djangocms_stories`` to your ``INSTALLED_APPS`` in your Django project's ``settings.py``:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'djangocms_stories',
        'parler',  # if not already included
        'sortedm2m',  # if not already included

        # For now, but probably not needed in the future
        'taggit',
        'taggit_autosuggest',
        'meta',
        # ...
    ]

To use taggit's autosuggest feature, add their URLS in ``urls.py``:

.. code-block:: python

    url_patterns += [path('taggit_autosuggest/', include('taggit_autosuggest.urls'))]


********
Features
********

* Placeholder content editing
* Frontend editing using django CMS frontend editor
* Multilingual support using django-parler
* Optional simpler TextField-based content editing
* Multisite (posts can be visible in one or more Django sites on the same project)
* Per-Apphook configuration
* Configurable permalinks
* Configurable user navigation (django CMS menu)
* Per-Apphook templates set
* Django sitemap framework
* django CMS Wizard integration
* Desktop notifications

*****************************
Migrating from djangocms-blog
*****************************

If you are migrating from djangocms-blog follow the steps below (at your own risk - the
migration is under development). Be sure to backup your database before.

1. Uninstall djangocsms-blog: ``pip uninstall djangocms-blog``
2. Install djangocms-stories ``pip install git+https://github.com/fsbraun/djangocms-stories.git``
3. Add ``"djangocms_stories"`` to your installed apps. Do **not** remove djangocms-blog.
4. Run ``./manage.py migrate djangocms_stories``. This in migration 0002 will move existing content
   from djangocms-blog to djangocms-stories and delete djangocms-blogs database tables.
5. Remove ``"djangocms_blog"`` from your installed apps.

************
Contributing
************

Contributions to ``djangocms-text`` are welcome! Please read our
`contributing guidelines <https://docs.django-cms.org/en/stable/contributing/index.html>`_
to get started.


.. |PyPiVersion| image:: https://img.shields.io/pypi/v/djangocms-stories.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-stories
    :alt: Latest PyPI version

.. |PyVersion| image:: https://img.shields.io/pypi/pyversions/djangocms-blog.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-stories
    :alt: Python versions

.. |TestCoverage| image:: https://img.shields.io/coveralls/fsbraun/djangocms-stories/master.svg?style=flat-square
    :target: https://coveralls.io/r/django-cms/djangocms-stories?branch=main
    :alt: Test coverage

.. |License| image:: https://img.shields.io/github/license/fsbraun/djangocms-stories.svg?style=flat-square
   :target: https://pypi.python.org/pypi/djangocms-stories/
    :alt: License
