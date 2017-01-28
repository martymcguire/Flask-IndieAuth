===============
Flask-IndieAuth
===============

This extension adds the ability to authorize requests to your Flask
endpoints via `IndieAuth <https://indieweb.org/IndieAuth>`_, using
``current_app.config['TOKEN_ENDPOINT']`` as the token server.

This is useful for developers of `Micropub <https://www.w3.org/TR/micropub/>`_
server implementations.

Configuration
=============

``current_app.config`` should contain the following configuration details:

:``TOKEN_ENDPONT``: (e.g. "https://tokens.indieauth.org/token")
:``ME``: (e.g. "http://example.com")

**Example Usage**::

    from flask_indieauth import requires_indieauth
    @app.route('/micropub', methods=['GET','POST'])
    @requires_indieauth
    def handle_micropub():
        ...

When a Flask route is wrapped in @requires_indieauth, this extension
will look for an IndieAuth bearer token in these locations in order:

* HTTP header ``Authorization: Bearer xxx...``
* HTTP form data in the parameter ``access_token``
* HTTP POST body, if in JSON format, in the ``access_token`` attribute

If an access token is found, it is checked for a ``me`` value equal to the
domain in ``current_app.config["ME"]`` and a ``scope`` value of ``post``.

If all checks pass, processing is passed to the Flask route handler.

Access Token Contents
---------------------

Upon successful authentication/authorization, Flask-IndieAuth will store
a ``user`` dict in `Flask.g <http://flask.pocoo.org/docs/0.12/api/#flask.g>`_ with
the following attributes:

:``me``: the homepage that the user logged in as
:``scope``: the authorization scope of this token
:``client_id``: typically the homepage for the micropub client
:``access_token``: the raw access token

**Example Usage**::

    from flask import g, current_app

    from flask_indieauth import requires_indieauth
    @app.route('/micropub', methods=['GET','POST'])
    @requires_indieauth
    def handle_micropub():
        user = g.user
        current_app.logger.info("Request from %s" % user["me"])
