from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{title}" with description "{description}" and due date "{due_date}"')
def step_impl(context, title, description, due_date):
    context.todo_list.add_task(title, description, due_date)

@then('the to-do list should contain "{title}"')
def step_impl(context, title):
    tasks = context.todo_list.list_tasks()
    assert any(title in task for task in tasks), f'Task "{title}" not found in the list.'

@given('the to-do list contains tasks')
def step_impl(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'], 'Sample description', '2024-08-01')

@then('the output should contain')
def step_impl(context):
    tasks = context.todo_list.list_tasks()
    for row in context.table:
        assert any(row['Tasks'] in task for task in tasks), f'Task "{row["Tasks"]}" not found in the list.'

@when('the user marks task "{title}" as completed')
def step_impl(context, title):
    result = context.todo_list.mark_task_completed(title)
    assert result, f'Could not mark task "{title}" as completed.'

@then('the to-do list should show task "{title}" as completed')
def step_impl(context, title):
    tasks = context.todo_list.list_tasks()
    assert any(f'{title} [Low] - Completed' in task for task in tasks), f'Task "{title}" not marked as completed.'

@when('the user removes the task "{title}"')
def step_impl(context, title):
    result = context.todo_list.remove_task(title)
    assert result, f'Could not remove task "{title}".'

@then('the to-do list should not contain "{title}"')
def step_impl(context, title):
    tasks = context.todo_list.list_tasks()
    assert not any(title in task for task in tasks), f'Task "{title}" is still in the list.'
