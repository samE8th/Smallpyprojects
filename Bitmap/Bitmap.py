class BitmapMessage:
    def __init__(self, bitmap):
        self.bitmap = bitmap

    def display_message(self, message):
        if not message:
            print("No message entered. Exiting.")
            return

        # Loop over each line in the bitmap:
        for line in self.bitmap.splitlines():
            # Loop over each character in the line:
            for i, bit in enumerate(line):
                if bit == ' ':
                    # Print an empty space since there's a space in the bitmap:
                    print(' ', end='')
                else:
                    # Print a character from the message:
                    print(message[i % len(message)], end='')
            print()  # Print a newline.


if __name__ == "__main__":
    bitmap = """....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................

    """

    print('Bitmap Message')
    print('Enter the message to display with the bitmap.')
    message = input('> ')

    bitmap_message = BitmapMessage(bitmap)
    bitmap_message.display_message(message)
