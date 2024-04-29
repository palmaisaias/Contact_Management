Contact Managemnt System Project
  -The purpose of the program is to allow the user to manage contacts by adding, editing, deleting, searching, and viewing all contacts.
  -Further, the program allows the user to store the contact file locally. The program has the capability of accessing and updating the 
  file in real time. The file is stored as a txt. file and will be accessible after you close the program. This inherently allows you to open the     program at a later time and still have access to your contacts list.

The program initiates with a welcome menu that provides the user 6 different options:

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/00ec8c04-58bc-4b05-af7d-e43a6ae3c824)

Add a New Contact:
Allows user to add a contact with 4 information categories 3 of these are required (Email, Name, Phone number) and Notes, being the fourth category , is optional for the user. Each of these is varified as a valid entry by the program using regex.

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/c7be2cbe-a765-4473-8eb8-9b9bfaf5f6a8)

Once the new contact has been verfied and added, thr program will print out a message confirming that the new contact has been added and consequently 
takes the user back to the main menu.

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/5e8cdcca-1dd2-4edb-b74f-375f8601a76a)

Edit An Existing Contact:
Allows user to edit an existing contact. When using this menu option the user will receive a list of all of their current contacts. Since the program uses email addressed as the unique identifier for each contact, providing the list at this point is convenient for the user. The user is prompted to enter the email of the contact they would like to edit or enter 'back' to return to the main menu. If there are no contacts on the users list/file, the program will populate a message stating that there are no currently no contacts. If the user enters an invalid email, they will be prompted that the email they have entered is not in their contacts.

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/d588e811-b2f6-4ccd-b6ba-6dbb4ab65e8f)
![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/5892d4af-87f7-4e48-b6d6-cd74d6bd5f4a)

When the user has chosen and entered the email of the contact they want to edit, they will be taken to a screen that gives them options for which portion of the contact they would like to edit.

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/24855ba6-ae90-4fa2-969b-f24e34138d45)

Every change will show the user the current value of the portion they want to edit and consequently ask the user what they want to update the information to...

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/3b7a2e92-4d1d-4a53-b0ff-c41522f24567)

Once the new information is entered, the program will confirm the update...

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/36233520-79c5-401f-b694-984c3b7b0588)

Delete Contact:
Allows user to delete an existing contact. When using this menu option the user will receive a list of all of their current contacts. The user is prompted to enter the email of the contact they wish to delete. If their entry does not match an email in their current list, they will receive a prompt stating to enter a valid email. Once a valid entry is entered, the user will receive a confirmation that the email and subsequent contact has been deleted.

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/e9358071-c716-412d-99c3-f22bcf02ad8b)

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/225ccbbf-327d-4b92-8eff-741e299defa0)

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/d6589d1c-25f2-40cd-bd73-852cd9460f60)

Search For Contact:
Allows the user to search for a contact using the email address. If the user inputs an email that is not in their contacts, they will receive a prompt stating that their entry is not an email in their contacts. Once the user has entered a valid email, the contact will populate along with all its pertaining information.

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/1e4d559f-d2e1-4974-ba64-1a4a441ab24b)

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/68dbc625-1803-4593-887c-61cbf6bcbaf8)

View All Contacts:
Allows user to view all current contacts in their list.

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/cbfd52ce-5d95-436d-8b62-148566f6ba73)

Quit:
Simply allows the user to end the program. The user will see a thnak you message and the program will end.

![image](https://github.com/palmaisaias/module_3_mini_proj/assets/158205305/f4ae82c2-cd6a-400f-8400-134bb5a8575d)



