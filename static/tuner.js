$( function() {
    $( "#sel" ) 
	.selectmenu()
	.selectmenu( "menuWidget" )
	.addClass( "overFlow" );
});


$(document).ready(function(){
    $("#jquery_jplayer_1").jPlayer({
	ready: function () {
	    $(this).jPlayer("setMedia", {
		title: "Synth",
		oga: "/static/synth.ogg"
	    });
	},
	cssSelectorAncestor: "#jp_container_1",
	swfPath: "/static",
	supplied: "oga",
	useStateClassSkin: true,
	autoBlur: false,
	smoothPlayBar: true,
	keyEnabled: true,
	remainingDuration: true,
	toggleDuration: true
    });
});


window.onload = function() {
    // Create an audio-context
    var audioContext = new window.AudioContext(),
	oscillator = audioContext.createOscillator();
    oscillator.type = 'sine';
    oscillator.frequency.value = 1500;
    oscillator.start();

    // Create an Oscilloscope instance
    //   Parameters:
    //     - The container in which the oschilloscope gets created
    //     - an optional audio-context on which the oscilloscope creates an analyser-node,
    //          and can connect to the destination.
    //          If no audio-context is specified, a new one will be created created.
    var oscilloscope = new Oscilloscope('.js-oscilloscope', audioContext);
    
    // Connect the oscillator-node to the oscilloscope
    oscillator.connect(oscilloscope.analyserNode);
    
    // Start the oscilloscope
    oscilloscope.start();
};
