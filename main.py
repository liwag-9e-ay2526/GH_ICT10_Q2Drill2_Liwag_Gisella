# ICT Drill 2: Working With Sets and Set Operators

from pyscript import document, display

# 4 Predefined sets of club members 
grade7 = {'Aubrey Graham', 'Rakim Mayers', 'Jahron Brathwaite'}
grade8 = {'Abel Tesfaye', 'Jacques Webster', 'Dominic Fike'}
grade9 = {'Solána Rowe', 'Shayaa Joseph', 'Tyler Okonma', 'Belcalis Almánzar'}
grade10 = {'Onika Maraj', 'Marshall Mathers', 'Stefani Germanotta', 'Belén Aguilera'}

def add_member(event):
    
    # Get values from the text boxes
    first_name = document.getElementById('fname').value
    last_name = document.getElementById('lname').value
    
    # Combine first and last name into string
    full_name = first_name + " " + last_name
    
    # Put the new member into set
    new_member_set = {full_name}
    
    # Combine all sets and the new member
    master_set = grade7 | grade8 | grade9 | grade10 | new_member_set
    
    # Get the total number of members
    total_members = len(master_set)
    
    # Output the result
    document.getElementById('output').innerHTML = f"""
        <h3>All members:</h3>
        <p>{master_set}</p>
        <h3>Total members: {total_members}</h3>
    """