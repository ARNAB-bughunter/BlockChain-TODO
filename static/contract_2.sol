pragma solidity ^0.5.0;

//without user

contract TodoList{
	uint public taskCount=0;
	
    struct Task{
        uint id;
        string content;
        bool completed;
	}
    
	mapping(uint => Task) public tasks;
    

	
	function createTask(string memory _content) public {
        taskCount ++;
		tasks[taskCount] = Task(taskCount,_content, false);
	}

    function markDone(uint _id) public {
        tasks[_id].completed=true;       
    }

    function updateTask(uint _id,string memory _content) public {
        tasks[_id]=Task(_id,_content,false);
    }

    function deleteTask(uint _id) public {
        delete(tasks[_id]);
    }

}