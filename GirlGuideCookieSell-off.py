def get_guide_amount():
    guide_amount = int(input("Enter the number of guides selling cookies: "))

    loop = 1
    guide_name = []
    boxes_sold = []

    while loop <= guide_amount:
        print("")
        name = input(f"Enter the name of Guide #{loop}: ")
        guide_name.append(name)
        boxes = int(input(f"Enter the amount of boxes sold by {name}: "))
        boxes_sold.append(boxes)
        loop += 1    

    return guide_name, boxes_sold



def avg_boxes(boxes_sold):
    
    average_boxes_sold = sum(boxes_sold) / len(boxes_sold)
    print(f"The average number of boxes sold by each guide was {average_boxes_sold:.1f}")

    return average_boxes_sold


def guide_prizes(boxes_sold, average_boxes_sold):

    prizes = []

    most_sold_prize = ("Trip to Girl Guide Jamboree in Aruba!")
    sold_above_avg_prize = ("Super Seller Badge")
    below_avg_above_one_prize = ("Left over cookies")

    highest_seller = max(boxes_sold)

    for box in boxes_sold:
        if box == highest_seller:
            prizes.append(most_sold_prize)
        elif box > average_boxes_sold:
            prizes.append(sold_above_avg_prize)
        elif box > 0 and box < average_boxes_sold:
            prizes.append(below_avg_above_one_prize)
        elif box == 0:
            prizes.append("")

    return prizes
    
    

def output(guide_name, prizes):
    print("Guide                      Prizes Won:")
    print("----------------------------------------------------------")

    for guide in range(len(guide_name)):
        print(f"{guide_name[guide]}\t\t- {prizes[guide]}")


def main():
    guide_name, boxes_sold = get_guide_amount()
    average_boxes_sold = avg_boxes(boxes_sold)
    prizes = guide_prizes(boxes_sold, average_boxes_sold)
    output(guide_name, prizes)

main()