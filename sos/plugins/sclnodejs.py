from sos.plugins import Plugin, SCLPlugin


class SCLNodeJS(Plugin, SCLPlugin):
    """
    Get runtime version of NodeJS from SCL collections that contain "nodejs"
    """

    requires_root = False
    packages = ("%(scl_name)s-nodejs",)
    profiles = ('system',)

    def setup(self):
        for scl in self.scls_matched:
            self.add_cmd_output_scl(scl, "node -v",
                                    suggest_filename="%s-nodejs-version" % scl)
