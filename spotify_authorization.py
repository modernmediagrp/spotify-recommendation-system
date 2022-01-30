#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Define an authorization function to run Spotify API.
Utilizing Tekore (https://github.com/felix-hilden/tekore)
to navigate Spotify's API.
"""

import tekore as tk

def authorize():
    client_id = 'ID_REDACTED' # Redacted API IDs for privacy reasons
    client_secret = 'ID_REDACTED' # Redacted API IDs for privacy reasons
    app_token = tk.request_client_token(client_id, client_secret)
    return tk.Spotify(app_token)

