import win32com.client
import sys

def get_scripting_task_state():
    TASK_ENUM_HIDDEN = 1
    TASK_STATE = {0: 'Unknown',
                  1: 'Disabled',
                  2: 'Queued',
                  3: 'Ready',
                  4: 'Running'}

    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()

    scripting_task = None

    folders = [scheduler.GetFolder('\\')]
    while folders:
        folder = folders.pop(0)
        folders += list(folder.GetFolders(0))
        tasks = list(folder.GetTasks(TASK_ENUM_HIDDEN))

        for task in tasks:
            if task.Path == r'\ScheduledTaskName':
                scripting_task = task
                break
        if scripting_task:
            break
    if scripting_task:
        scripting_task_state = TASK_STATE[scripting_task.State]
        return scripting_task_state
    else:
        print('Task not found. Aborting.')
        sys.exit()


state = get_scripting_task_state()
print('this is the task state: {}'.format(state))
