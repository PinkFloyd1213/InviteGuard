from modubot import PropertyDict

class HelpConfig(PropertyDict):
    invite_url: str = "https://discord.com/oauth2/authorize?client_id=1196435760279195750&scope=bot&permissions=2415920129"
    github_url: str = "https://github.com/PinkFloyd1213/InviteGuard"
    privacy_policy_url: str = "https://gist.github.com/PinkFloyd1213/7ffd080945f57048a062d8767e2ed008"
    credit_url: str = "https://github.com/wow13524/invite-role-bot"

class InviteRoleBotConfig(PropertyDict):
    help_command: HelpConfig = HelpConfig([],{},"")