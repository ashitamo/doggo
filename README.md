venv建立

`virtualenv venv`

Cmd + Shift + P 

select interpreter =>.venv

右下按是

Cmd + Shift + P

python create terminal


**喜悅**

當狗狗喜悅時，身體會呈現彎曲並興奮地不停跳動，甚至會有前腳踏地或尾巴劇烈左右搖晃，叫聲會顯得明亮有力，年紀較小的狗可能會有情緒較為失控的情況，長大後會有改善。

**愉快**

愉快的狗狗情緒會比喜悅在穩定一些，動作會有尾巴輕微搖晃、輕舔主人的手或是親暱的待在身邊，在對人表示好感時能夠聽見狗狗用喉嚨發出「嗚嗚」的聲音。

**撒嬌**

狗狗撒嬌分為兩種，一種是因犯錯想求主人原諒，另一種是乞求東西或是要求主人陪玩的時候。前者會將尾巴垂下，後者則揚起微微晃動，撒嬌的聲音為「呵呵」。

**憤怒**

憤怒的狗狗最明顯的就是會牙齒外翻，用較為低沉的聲音發出「嗚嗚」聲，藉以威脅對方，同時身體會變僵直、伸展四肢等動作，耳朵會豎起朝向對方。

**悲傷**

狗狗在悲傷時會將尾巴垂下，發出悲鳴聲以訴求自己的悲傷、痛苦，並以低姿態的身姿摩蹭主人。

**警覺**

當狗狗察覺到危險，變得警覺的時候會將耳朵豎立起來，嘗試聽清楚附近的聲音，並且發出「汪汪」的警告聲，若是危險持續接近，狗狗也會將叫聲拉長且不斷續。

**恐懼**

狗狗恐懼時，會依不同程度的恐懼而垂下尾巴，若尾巴以垂到最低並收到兩腿之間，就是狗狗覺得最害怕的時刻，耳朵向後低垂、身體縮成一團也都是狗狗害怕時的反應。

即使不會開口說話，只要主人抱持著愛心，仔細觀察自己的毛小孩，還是可以了解牠們的喔


function simulateRightClick( element ) {
    var event1 = new MouseEvent( 'mousedown', {
        bubbles: true,
        cancelable: false,
        view: window,
        button: 2,
        buttons: 2,
        clientX: element.getBoundingClientRect().x,
        clientY: element.getBoundingClientRect().y
    } );
    element.dispatchEvent( event1 );
    var event2 = new MouseEvent( 'mouseup', {
        bubbles: true,
        cancelable: false,
        view: window,
        button: 2,
        buttons: 0,
        clientX: element.getBoundingClientRect().x,
        clientY: element.getBoundingClientRect().y
    } );
    element.dispatchEvent( event2 );
    var event3 = new MouseEvent( 'contextmenu', {
        bubbles: true,
        cancelable: false,
        view: window,
        button: 2,
        buttons: 0,
        clientX: element.getBoundingClientRect().x,
        clientY: element.getBoundingClientRect().y
    } );
    element.dispatchEvent( event3 );
}
function getURLParam( queryString, key ) {
    var vars = queryString.replace( /^\?/, '' ).split( '&' );
    for ( let i = 0; i < vars.length; i++ ) {
        let pair = vars[ i ].split( '=' );
        if ( pair[0] == key ) {
            return pair[1];
        }
    }
    return false;
}
function createDownload( contents ) {
    var hiddenElement = document.createElement( 'a' );
    hiddenElement.href = 'data:attachment/text,' + encodeURI( contents );
    hiddenElement.target = '_blank';
    hiddenElement.download = 'urls.txt';
    hiddenElement.click();
}
function grabUrls() {
    var urls = [];
    return new Promise( function( resolve, reject ) {
        var count = document.querySelectorAll(
        	'.isv-r a:first-of-type' ).length,
            index = 0;
        Array.prototype.forEach.call( document.querySelectorAll(
        	'.isv-r a:first-of-type' ), function( element ) {
            // using the right click menu Google will generate the
            // full-size URL; won't work in Internet Explorer
            // (http://pyimg.co/byukr)
            if (element.querySelector( ':scope img' )){
                simulateRightClick( element.querySelector( ':scope img' ) );
                // Wait for it to appear on the <a> element
                var interval = setInterval( function() {
                    if ( element.href.trim() !== '' ) {
                        clearInterval( interval );
                        // extract the full-size version of the image
                        let googleUrl = element.href.replace( /.*(\?)/, '$1' ),
                            fullImageUrl = decodeURIComponent(
                                getURLParam( googleUrl, 'imgurl' ) );
                        if ( fullImageUrl !== 'false' ) {
                            urls.push( fullImageUrl );
                        }
                        // sometimes the URL returns a "false" string and
                        // we still want to count those so our Promise
                        // resolves
                        index++;
                        if ( index == ( count - 1 ) ) {
                            resolve( urls );
                        }
                    }
                }, 10 );
            }
        } );
    } );
}
grabUrls().then( function( urls ) {
    urls = urls.join( '\n' );
    createDownload( urls );
} );