def run(*name):
    for kids in name:
        print(f'{kids} ran like a fool!')

run("Timmy", "Jimmy", "Gimmy")

def swing(*name):
    for kids in name:
        print(f'{kids} swings high!')

swing("Timmy", "Jimmy", "Gimmy", "Sally")


def slide(*name):
    for kids in name:
        print(f'{kids} slides like a bullet!')

slide("Timmy", "Jimmy", "Gimmy", "Sally", "Roger")


def hide_and_seek(*name):
    for kids in name:
        print(f'{kids} hides and seeks like a pro!')

hide_and_seek("Timmy", "Jimmy", "Gimmy", "Sally", "Roger", "DJ")
