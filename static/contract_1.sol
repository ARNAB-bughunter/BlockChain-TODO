pragma solidity ^0.5.1;

//with user

contract MyContract{
    
    struct Task{
        string taskName;
        bool isDone;        
    }

    mapping(address => Task[] ) private Users;

    function createTask(string memory _taskName) public{
        Users[msg.sender].push(Task(_taskName, false));
    }

    function markDone(uint _index) public{
        Users[msg.sender][_index].isDone = true;
    }

    function updateTask(uint _index,string memory _taskName) public {
        Users[msg.sender][_index].taskName=_taskName;
    }

    function deleteTask(uint _index) public{
        delete Users[msg.sender][_index];
    }

	function getTaskCount() external view returns (uint256){
	return Users[msg.sender].length;
	} 

}