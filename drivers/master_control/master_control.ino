#include <ArduinoHardware.h>
#include <ros.h>
#include <Stepper.h> 
#include <geometry_msgs/Twist.h>
#define Pi 3.14159265


// Define stepper motor connections and motor interface type. Motor interface type must be set to 1 when using a driver
const int stepsPerRevolution = 150;
Stepper stepper(stepsPerRevolution, 8, 9, 10, 11); // Pin 2 connected to DIRECTION & Pin 3 connected to STEP Pin of Driver
#define motorInterfaceType 1

// For Motor Controller
int motor1pin1 = 2;
int motor1pin2 = 3;
int motor2pin1 = 4;
int motor2pin2 = 5;


//change pins
int enA = 9;
int enB = 10;

// For Steering Stepper
int theta = 0; // Target steering angle
int curr_steer = 0; // current Steering angle
int step_multiplier = 6; // Multiplier for Gear Ratio
float speed_ang = 0;
float speed_lin = 0;


ros::NodeHandle nh;

void messageCb( const geometry_msgs::Twist& msg){
  speed_ang = msg.linear.y;
  speed_lin = msg.linear.x;
//  int w_r = (speed_lin/wheel_rad) + ((speed_ang*wheel_sep)/(2.0*wheel_rad));
//  int w_l = (speed_lin/wheel_rad) - ((speed_ang*wheel_sep)/(2.0*wheel_rad));
}

ros::Subscriber<geometry_msgs::Twist> sub("steervel_pub", &messageCb );
 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);
  nh.getHardware()->setBaud(57600);

  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(motor2pin1, OUTPUT);
  pinMode(motor2pin2, OUTPUT);

//Change
//  pinMode(9, OUTPUT); 
//  pinMode(10, OUTPUT);

  //Stepper
  stepper.setSpeed(1000);
  // Node
  nh.initNode();
  nh.subscribe(sub);
}

 

void loop() {
  
  //Controlling speed (0 = off and 255 = max speed):
//  analogWrite(9, 255); //ENA pin
//  analogWrite(10, 255); //ENB pin
  float potValue1 = 1.0;
  float potValue2 = 5.0;// Read potentiometer value
  int pwmOutput1 = map(potValue1, 0, 5, 0 , 255); // Map the potentiometer value from 0 to 255
  int pwmOutput2 = map(potValue2, 0, 5, 0 , 255); // Map the potentiometer value from 0 to 255

//  Serial.print(pwmOutput1);/
  analogWrite(enA, pwmOutput1); // Send PWM signal to L298N Enable pin
  analogWrite(enB, pwmOutput2);

  //Controlling spin direction of motors:
  //Motor 1
  digitalWrite(motor1pin1, HIGH);
  digitalWrite(motor1pin2, LOW);
  //Motor 2
  digitalWrite(motor2pin1, HIGH);
  digitalWrite(motor2pin2, LOW);

  // Step_count the final angle for steering to move
  theta = speed_ang * 180/Pi;
  int step_count  = theta - curr_steer;
  int final_steps = step_count * step_multiplier;

//  stepper.step(final_steps);
  stepper.step(100);
  curr_steer = theta;
//  for (int i = 0; i< 20; i++){
//      stepper.step(100);
////      Serial.println(i);
//      delay(10);
//  }
//  for (int i = 0;i < 20; i++){
//      stepper.step(-100);
//      delay(10);
//  }
  nh.spinOnce();
  delay(1);

}
