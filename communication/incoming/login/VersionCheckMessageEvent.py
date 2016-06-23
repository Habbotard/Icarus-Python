import util.logging as log


class VersionCheckMessageEvent:
    def handle(self, session, message):
        """
        Handle login request
        :param session: the session who requests CheckReleaseMessageEvent handler
        :param message: the incoming message with login details
        """

        log.info("Version check, swf revision: " + message.read_string())