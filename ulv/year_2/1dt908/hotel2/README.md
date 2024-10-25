# Hotel2

## How to run application

1. Install Docker Desktop (on Windows or Mac) or Docker on Linux
2. On Windows or Mac start docker desktop. On Linux start the docker daemon
3. Run `docker-compose up -d` from the docker directory in the terminal, on Linux `sudo docker-compose up -d` in the docker directory
4. Go to the hotel2 directory & run the application with `gradle run` or `./gradlew run`
5. You can use the following test accounts to use the application:

```text
Format: username -- password

-- General
admin -- Admin
reception -- toor

-- Admistrator
tobias -- tobias@hotel2
imad -- imad@hotel2

-- Receptionist
jesper -- jesper@hotel2
emil -- emil@hotel2
samuel -- samuel@hotel2
tobias1 -- tobias1@hotel2
```

## Known bugs and issues

```text
Bug:
When creating a new booking you can add two of the same room.

How to reproduce the bug:
1. Go into create new booking.
2. Add a room for example room 101.
3. Click 'Färdig' and go to add a new room.
4. Add the same room again.
```

```text
Bug:
When opening the settings menu it rotates incorrectly

How to reproduce the bug:
1. Click the settings icon.
2. Click anywhere on the scrren except on the dropdown menu or the icon.
3. Click on the settings icon again and the menu opens but the rotation is the wrong way.
```

```text
Bug:
When logging into an account the username is not case sensitive.

How to reproduce the bug:
1. Login with the username with random letters capitalized for exapmple.
```

```text
Bug:
On non-Mac devices when multiple pop-up windows are created the windows hide eachother and the application becomes hardlocked.

How to reproduce the bug:
1. Click on either the button for "ny bokning" or "Hantera gäster" or click on the settings icon and then "Ändra profil"
2a. In "ny bokning" click on "Ny gäst"
3a. Fill in the information of the guest and press "Skapa gäst"
2b. In "Hantera gäster" click on "Skapa ny gäst"
3b. Fill in the information of the guest and press "Skapa gäst"
2c. Fill in the information and click on "Uppdatera profil"
```
