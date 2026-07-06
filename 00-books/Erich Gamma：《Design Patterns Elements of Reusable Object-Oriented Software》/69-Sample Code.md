3. Creating and destroying State objects. A common implementation trade-off worth considering is whether (1) to create State objects only when they are needed and destroy them thereafter versus (2) creating them ahead of time and never destroying them.

The first choice is preferable when the states that will be entered aren’t known at run-time, and contexts change state infrequently. This approach avoids creating objects that won’t be used, which is important if the State objects store a lot of information. The second approach is better when state changes occur rapidly, in which case you want to avoid destroying states, because they may be needed again shortly. Instantiation costs are paid once up-front, and there are no destruction costs at all. This approach might be inconvenient, though, because the Context must keep references to all states that might be entered.

4 . Using dynamic inheritance. Changing the behavior for a particular request could be accomplished by changing the object’s class at run-time, but this is not possible in most object-oriented programming languages. Exceptions include Self [US87] and other delegation-based languages that provide such a mechanism and hence support the State pattern directly. Objects in Self can delegate operations to other objects to achieve a form of dynamic inheritance. Changing the delegation target at run-time effectively changes the inheritance structure. This mechanism lets objects change their behavior and amounts to changing their class.

## Sample Code

The following example gives the C++ code for the TCP connection example described in the Motivation section. This example is a simplified version of the TCP protocol; it doesn’t describe the complete protocol or all the states of TCP connections.<sup>8</sup>

First, we define the class TCPConnection, which provides an interface for transmitting data and handles requests to change state.

class TCPOctetStream;   
class TCPState;   
classTCPConnection {   
public:   
TCPConnection();   
void ActiveOpen();   
void PassiveOpen();   
void Close();   
void Send();   
void Acknowledge();   
void Synchronize();   
void ProcessOctet (TCPOctetStream\*);   
private:   
friend class TCPState;   
void ChangeState(TCPState\*);   
private:   
TCPState\*\_state;   
};

TCPConnection keeps an instance of the TCPState class in the \_state member variable. The class TCPState duplicates the state-changing interface of TCPConnection. Each TCPState operation takes a TCPConnection instance as a parameter, letting TCPState access data from TCPConnection and change the connection’s state.

class TCPState {   
public:   
virtual void Transmit(TCPConnection\*, TCPOctetStream\*);   
virtualvoidActiveOpen(TCPConnection\*);   
virtual void PassiveOpen(TCPConnection\*);   
virtual void Close(TCPConnection\*);   
virtual void Synchronize(TCpConnection\*);   
virtual void Acknowledge(TCPConnection\*);   
virtual void Send(TCPConnection\*);   
protected:   
void ChangeState(TCPConnection\*, TCPState\*);   
);

TCPConnection delegates all state-specific requests to its TCPState instance \_state. TCPConnection also provides an operation for changing this variable to a new TCPState. The constructor for TCPConnection initializes the object to the TCPClosed state (defined later).

TCPConnection::TCPConnection () {   
\_state= TCPClosed::Instance();   
1   
void TCPConnection::ChangeState (TCPState\*s){   
\_state = s;   
  
void TCPConnection::ActiveOpen () {   
\_state->ActiveOpen(this);   
void TCPConnection::PassiveOpen () {   
\_state->PassiveOpen(this);   
  
void TCPConnection::Close(){   
\_state->Close(this);   
void TCPConnection::Acknowledge () (   
\_state->Acknowledge(this);   
void TCPConnection::Synchronize(){   
\_state->Synchronize(this);

TCPState implements default behavior for all requests delegated to it. It can also change the state of a TCPConnection with the ChangeState operation. TCPState is declared a friend of TCPConnection to give it privileged access to this operation.

void TCPState::Transmit (TCPConnection\*, TCPOctetStream\*){}   
void TCPState::ActiveOpen (TCPConnection\*){}   
void TCPState::PassiveOpen (TCPConnection\*){}   
void TCPState::Close (TCPConnection\*){ }   
void TCPState::Synchronize (TCPConnection\*){}   
void TCPState::ChangeState (TCPConnection\* t, TCPState\* s){   
t->ChangeState(s);   
}

Subclasses of TCPState implement state-specific behavior. A TCP connection can be in many states: Established, Listening, Closed, etc., and there’s a subclass of TCPState for each state. We’ll discuss three subclasses in detail: TCPEstablished, TCPListen, and TCPClosed.

class TCPEstablished : public TCPState {   
public:   
static TCPState\* Instance();   
virtual void Transmit(TCPConnection\*, TCPOctetStream\*);   
virtualvoid Close(TCPConnection\*);   
class TCPListen : public TCPState {   
public:   
static TCpState\* Instance();   
virtualvoid Send(TCPConnection\*);   
class TCPClosed: public TCPState {   
public:   
static TCpState\* Instance();   
virtual void ActiveOpen(TCPConnection\*);   
virtual void PassiveOpen(TCPConnection\*);

TCPState subclasses maintain no local state, so they can be shared, and only one instance of each is required. The unique instance of each TCPState subclass is obtained by the static Instance operation.<sup>9</sup>

Each TCPState subclass implements state-specific behavior for valid requests in the state: