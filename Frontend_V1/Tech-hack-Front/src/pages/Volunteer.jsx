import React, {useState} from 'react'
// import Select from 'react-select'
import {ChatWidget} from 'react-chat-widget';
import 'react-chat-widget/lib/styles.css';


const Volunteer = ()=>  {
    const [selectedOption, setSelectedOption] = useState('');
    const [showChat, setShowChat] = useState(false);
    // const options = [
    //     { value: 'Traffic management', label: 'Traffic Management' },
    //     { value: 'Road Quality', label: 'Road Quality' },
    //     { value: 'Real Time Accidents', label: 'Real Time Accidents' }
    //   ]

   const handleChatClick=()=> {
        setShowChat(true);
      }

      const handleOptionChange=(event)=> {
        setSelectedOption(event.target.value);
      }

  return (
    // <div className='text-black flex justify-center'>
    <div className='text-black flex justify-center'>
    <label htmlFor="menu">Choose an option:</label>
    <select id="menu" value={selectedOption} onChange={handleOptionChange}>
      <option value="">--Please choose an option--</option>
      <option value="Traffic-Management">Traffic-Management</option>
      <option value="Road-Quality">Road-Quality</option>
      <option value="Real-time Accidents">Real-time Accidents</option>
    </select>
    <p>You selected: {selectedOption}</p>
    <div>
      <h1>Traffic section</h1>
      <button onClick={handleChatClick}>Open Chat</button>
      {showChat && (
        <ChatWidget
          title="Chat with us"
          senderPlaceHolder="Type a message..."
          showCloseButton={true}
          handleNewUserMessage={(newMessage) =>
            console.log(`New message incoming! ${newMessage}`)
          }
        />
      )}
    </div>
  </div>
);
}

export default Volunteer