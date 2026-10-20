from pyscript import document

club_members = ["Ishabel Manaloto", "Lyxander Squishy", "Doggie Dog"]


def check_name(e):
  first = document.getElementById("first_name").value.strip()
  last = document.getElementById("last_name").value.strip()

  full_name = first + " " + last

  result = full_name in club_members

  messages = {
      True: (
          "Congratulations "
          + full_name
          + "! You are now part of the ICT club. ♡"
      ),
      False: "Sorry " + full_name + ", your name is not on the list.",
  }

  document.getElementById("result").innerHTML = messages[result]