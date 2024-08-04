from utilities.config import ScanConfigurations


class Headers:
    def __init__(self, confg=None):
        self.confg = 'HEADERS' if confg is None else confg
        self.hdr_user_agent = ScanConfigurations(self.confg, 'User-Agent').getvalue()
        self.hdr_rqst_with = ScanConfigurations(self.confg, 'X-Requested-With').getvalue()
        self.hdr_acpt_enco = ScanConfigurations(self.confg, 'Accept-Encoding').getvalue()
        self.hdr_accept = ScanConfigurations(self.confg, 'Accept').getvalue()
        self.hdr_conn_stat = ScanConfigurations(self.confg, 'Connection').getvalue()

    def getDefaultHeader(self):
        return {'User-Agent': self.hdr_user_agent,
                'X-Requested-With': self.hdr_rqst_with,
                'Accept-Encoding': self.hdr_acpt_enco,
                'Accept': self.hdr_accept,
                'Connection': self.hdr_conn_stat}