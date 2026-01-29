# ok
from pyscript import display, document

def team_identity(e):
    document.getElementById('result').innerHTML =  '    '
    reg = document.getElementById('reg').value
    cert = document.getElementById('cert').value
    grade = document.getElementById('grade').value
    section = document.getElementById('section').value
    
    if reg == "Yes" and cert == "Yes" and grade == "7" and section == "eme":
        display(f'Congrats, you are blue bears', target='result')

    elif reg == "Yes" and cert == "No" and grade == "7" and section == "eme":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "7" and section == "eme":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "7" and section == "eme":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "8" and section == "eme":
        display(f'Congrats, you are blue bears', target='result')

    elif reg == "Yes" and cert == "No" and grade == "8" and section == "eme":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "8" and section == "eme":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "8" and section == "eme":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "9" and section == "eme":
        display(f'Congrats, you are blue bears', target='result')

    elif reg == "Yes" and cert == "No" and grade == "9" and section == "eme":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "9" and section == "eme":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "9" and section == "eme":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "10" and section == "eme":
        display(f'Congrats, you are yellow tigers', target='result')

    elif reg == "Yes" and cert == "No" and grade == "10" and section == "eme":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "10" and section == "eme":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "10" and section == "eme":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "7" and section == "ruby":
        display(f'Congrats, you are red bulldogs', target='result')

    elif reg == "Yes" and cert == "No" and grade == "7" and section == "ruby":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "7" and section == "ruby":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "7" and section == "ruby":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "8" and section == "ruby":
        display(f'Congrats, you are blue bears', target='result')

    elif reg == "Yes" and cert == "No" and grade == "8" and section == "ruby":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "8" and section == "ruby":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "8" and section == "ruby":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "9" and section == "ruby":
        display(f'Congrats, you are red bulldogs', target='result')

    elif reg == "Yes" and cert == "No" and grade == "9" and section == "ruby":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "9" and section == "ruby":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "9" and section == "ruby":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "10" and section == "ruby":
        display(f'Congrats, you are blue bears', target='result')

    elif reg == "Yes" and cert == "No" and grade == "10" and section == "ruby":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "10" and section == "ruby":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "10" and section == "ruby":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "7" and section == "sapph":
        display(f'Congrats, you are yellow tigers', target='result')

    elif reg == "Yes" and cert == "No" and grade == "7" and section == "sapph":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "7" and section == "sapph":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "7" and section == "sapph":
        display(f'Not eligible', target='result')

    else:
        display(f'invalid', target='result')
        