BOT_NAME = "vacancy"

SPIDER_MODULES = ["vacancy.spiders"]
NEWSPIDER_MODULE = "vacancy.spiders"

ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
