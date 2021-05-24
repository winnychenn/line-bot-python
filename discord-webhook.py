#!/usr/bin/env python3
# coding=utf8

from discord_webhook import DiscordWebhook


content = 'test <@350265813695201280>'
allowed_mentions = {
    "parse": ["everyone"],
    "users": []
}

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/831066944509444136/VqG1tFw2EIT25eIXoWptsDoA_h8cWQmJy6qOc4w3brrdmBWN_8P7wYgItd4gvNtiOT9z', content=content)
response = webhook.execute()

