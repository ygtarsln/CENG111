def line111(text, cmds):
    """
    Apply the specified commands to the text (a single string) as the totally awesome line111
    editor. Remember that "pos" commands do not count for undo/redo! Return
    the final, new text!

    text:   A string. The text that will be modified by the commands. Only
            contains letters and numbers.
    cmds:   A list of strings. Commands to be applied to the text sequentially.
            Explained in the description.
    """
    cursor = 0
    undo_stack = [text]
    for cmd in cmds:
        command = cmd.split(" ")[0]
        if command == "pos":
            i = int(cmd.split(" ")[1])
            if i >= len(text):
                cursor = len(text)
            else:
                cursor = i
        if command == "ins":
            sttr = cmd.split(" ")[1]
            if cursor == 0:
                text = sttr + text
            else:
                text = text[:cursor] + sttr + text[cursor:]
            undo_stack.append(text)
        if command == "del":
            if cursor == 0:
                text = text[1:]
            else:
                text = text[:cursor] + text[cursor+1:]
            undo_stack.append(text)
        if command == "undo":
            if undo_stack == []:
                continue
            else:
                if len(undo_stack) == 1:
                    text = undo_stack.pop()
                else:
                    undo_stack.pop()
                    text = undo_stack[-1]
    return text