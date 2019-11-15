# /*    
 # * StepperMotorTest.py 
 # * This is a test code  for BBG/BBB motor bridge cape Stepper Motor
 # *   
 # * Copyright (c) 2015 seeed technology inc.  
 # * Author      : Jiankai Li  
 # * Create Time:  Nov 2015
 # * Change Log : 
 # *
 # * The MIT License (MIT)
 # *
 # * Permission is hereby granted, free of charge, to any person obtaining a copy
 # * of this software and associated documentation files (the "Software"), to deal
 # * in the Software without restriction, including without limitation the rights
 # * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # * copies of the Software, and to permit persons to whom the Software is
 # * furnished to do so, subject to the following conditions:
 # * 
 # * The above copyright notice and this permission notice shall be included in
 # * all copies or substantial portions of the Software.
 # * 
 # * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # * THE SOFTWARE.
 # */
 

import MotorBridge
import time
import sys

def StepperMotorATest():
    print 'Hello From MotorBridge'
    motor.StepperMotorAInit()
    motor.StepperMotorAMove(int(sys.argv[2]),int(sys.argv[3])) # 1000 steppers  1000us every step
    time.sleep(1)
    motor.StepperMotorAMove(int(sys.argv[2]),int(sys.argv[3])) # 1000 steppers  1000us every step
    time.sleep(1)
    
def StepperMotorBTest():
    print 'Hello From MotorBridge'
    motor.StepperMotorBInit()
    motor.StepperMotorBMove(int(sys.argv[2]),int(sys.argv[3])) # 1000 steppers  1000us every step
    time.sleep(1)
    motor.StepperMotorBMove(int(sys.argv[2]),int(sys.argv[3])) # 1000 steppers  1000us every step
    time.sleep(1)

    
if sys.argv[1]=A:
    motor = MotorBridge.MotorBridgeCape()
    while True:
        StepperMotorATest()
     
elif sys.argv[1]=B:    
    motor = MotorBridge.MotorBridgeCape()
    while True:
        StepperMotorBTest()
     
else:
    motor = MotorBridge.MotorBridgeCape()
    while True:
        StepperMotorATest()
        StepperMotorBTest()
    
