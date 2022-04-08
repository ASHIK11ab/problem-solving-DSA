#include<iostream>
using namespace std;

// Returns whether a character is in lowercase or not.
int islower(char ch) {
  return int(ch) >= 97 && int(ch) <= 122;
}


// Returns whether a character is in uppercase or not.
int isupper(char ch) {
  return int(ch) >= 65 && int(ch) <= 90;
}


// Compares two strings (irrespective of case).
int cmp(char str1[], char str2[]) {
  int i1 = 0;
  int i2 = 0;
  while(str1[i1] != '\0' || str2[i2] != '\0') {
    /* String 1 has ended and string 2 has some more characters.
      string 1 is less than string 2. */
    if(str1[i1] == '\0' && str2[i2] != '\0')
      return -1;
      
    /* String 1 has not ended and string 2 has ended.
      string 1 is greater than string 2. */
    if(str1[i1] != '\0' && str2[i2] == '\0')
      return 1;

    // When case of both the characters are different.
    if(islower(str1[i1]) && isupper(str2[i1]))
      return -1;
    
    if(isupper(str1[i1]) && islower(str2[i2]))
      return 1;

    // When string 1 is less than string 2.
    if(str1[i1] < str2[i2])
      return -1;
    else
      // When string 1 is greater than string 2.
      if(str1[i1] > str2[i1])
        return 1;
    
    i1++;
    i2++;
  }
  // when string 1 is equal to string 2.
  return 0;
}


void swap_in_array(char names[][100], int i, int j) {
  int i1 = 0, i2 = 0;
  int a_end_reached = 0;
  int a_end_pos = -1;
  int b_end_reached = 0;
  int b_end_pos = -1;
  char temp;

  while(names[i][i1] != '\0' || names[j][i2] != '\0') {
    /* Prevent the if check from always evalutaing to true. String will
      always be at '\0' since the pointers i1 and i2 are not incremented.*/
    if(names[i][i1] == '\0' && ! a_end_reached) {
      a_end_reached = 1;
      a_end_pos = i1;
      continue;
    }

    /* Prevent the if check from always evalutaing to true. String will
      always be at '\0' since the pointers i1 and i2 are not incremented.*/
    if(names[j][i2] == '\0' && ! b_end_reached) {
      b_end_reached = 1;
      b_end_pos = i1;
      continue;
    }

    /* Attach ele's from 2nd string to first string.
      First string is less in size. */
    if(a_end_reached)
      names[i][i1] = names[j][i2];
    else
      /* Attach ele's from 1st string to second string.
        second string is less in size. */
      if(b_end_reached)
        names[j][i2] = names[i][i1];
      // Swap the characters from both the strings.
      else {
        temp = names[i][i1];
        names[i][i1] = names[j][i2];
        names[j][i2] = temp;
      }
    
    i1++;
    i2++;
  }

  // Set '\0' for the swapped strings.
  names[i][b_end_pos] = '\0';
  names[j][a_end_pos] = '\0';
}

int main() {
  int size;
  cout<<"Enter size: ";
  cin>>size;
  char names[size][100];
  int i, j;

  for(i = 0; i < size; ++i) {
    cin>>names[i];
  }

  cout<<"\nArray Before swapping:\n";
  cout<<"[ ";
  for(i = 0; i < size-1; ++i)
    cout<<names[i]<<", ";
  cout<<names[i]<<" ]";

  for(i = 0; i < size; ++i) 
    for(j = 0; j < size - i - 1; ++j)
      if(cmp(names[j], names[j+1]) == 1)
        swap_in_array(names, j, j+1);

  cout<<"\n\nArray after swapping:\n";
  cout<<"[ ";
  for(i = 0; i < size-1; ++i)
    cout<<names[i]<<", ";
  cout<<names[i]<<" ]";
}