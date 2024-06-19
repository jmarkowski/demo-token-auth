# demo-token-auth

Herein is a basic demonstration of token-based authentication.

Token-based authentication allows a user to be authenticated using a token
instead of requiring a password to access endpoints. It acts as a secure
credential that proves the user's identity, allowing for stateless operation and
secure transmission of user identity information (e.g. ID, permissions, etc.)

# How it works

At a high-level, there are 3 steps.

1. A registered user is authenticated by logging in.
2. If the login information is successfully verified, a token is generated and
sent to the user.
3. The user provides the token in all of its requests, whereby the server validates it.

A token is generated and verified with a digital signature.

# Resources

[Token-based Authentication and
JWTs](https://www.swequiz.com/learn/token-based-auth-jwt-json-web-tokens)
