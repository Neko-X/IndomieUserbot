from indomie import BOT_USERNAME, CMD_HELP, bot
from indomie.utils import edit_or_reply, edit_delete, indomie_cmd

user = bot.get_me()
DEFAULTUSER = user.first_name
CUSTOM_HELP_EMOJI = "✘"


@indomie_cmd(pattern="helps ?(.*)")
async def cmd_list(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, f"**✘ Commands available in {args} ✘** \n\n" + str(CMD_HELP[args]) + "\n\n**☞ @IndomieProject**")
        else:
            await edit_delete(event, f"**Module** `{args}` **Tidak tersedia!**")
    else:
        try:
            results = await bot.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "@IndomieUserbot"
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except BaseException:
            await edit_delete(event,
                              f"** Sepertinya obrolan atau bot ini tidak mendukung inline mode.**"
                              )
