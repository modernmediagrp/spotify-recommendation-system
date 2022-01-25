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
    client_id = '4eb9684aba474efa92f55be38917497e'
    client_secret = '80f447a4ac9a40ef99dac84fc345e3b9'
    app_token = tk.request_client_token(client_id, client_secret)
    return tk.Spotify(app_token)

