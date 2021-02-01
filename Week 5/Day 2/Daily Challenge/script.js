
var cityValue = document.getElementById("city");
var monsterValue = document.getElementById("monster");
var nameValue = document.getElementById("person");
var name2Value = document.getElementById("person2");




let libButton = document.getElementById('lib-button');
        let libIt = function() {
            if(cityValue.value.length != 0 && monsterValue.value.length != 0 && nameValue.value.length != 0 && name2Value.value.length != 0){
                
                let storyDiv = document.getElementById("story");
            storyDiv.innerHTML ="There was a haunted house in " + cityValue.value + " 'It is very scary', said " +  nameValue.value + " and " + name2Value.value + " replied, 'Yes, I am very scared'.They both went through the black, creaky gates. As they walked to the house they saw a "  +  monsterValue.value +  " lurking in the dark. They both screamed very loud saying, 'Argghhh! Its a "  +  monsterValue.value + " And they both got torn to shreds. "
            
            }
            else{
                let storyDiv = document.getElementById("story");
                storyDiv.innerHTML = "You need to fill up the forms please"
            }
            
        };
        libButton.addEventListener('click', libIt);