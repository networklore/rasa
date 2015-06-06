RASA: A Python wrapper for the Cisco ASA REST API
=================================================

Rasa is a Rest API wrapper for the Cisco ASA 9.3 and later. It is currently
Alpha code but can be used for testing

WARNING: As this is under early development it might change making current code incompatible.

Known Issues
------------

- Doesn't handle offsets, this will be added in future releases (limits the number of returned objects to 100)
- Certificates, you can't yet specify which certificates to use. Only enable or disable checks

