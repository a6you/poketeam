class Pokemon extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
        <div class="pokemon">
            <div class="top info">
                <div class="icon">Garchomp</div>
                <div class="icon level">Lv. 100<img class="gender" src="other-icons/male-icon.png" alt=""></div>
                <div class="icon">Rough Skin</div>
                <div class="icon"><img class="info-pic" src="items/rocky-helmet.png" alt="">Rocky Helmet</div>
            </div>
            <div class="top type-profile">
                <div class="icon typebox">
                    <img class="type" src="types/regular/dragon.png" alt="">
                    <img class="type" src="types/regular/ground.png" alt="">
                    <div style="width: 0.50px; height: 20px; background: #D9D9D9; opacity: 0.3; margin-left: 1px; margin-right: 1px;"></div>
                    <img class="type" src="types/tera/ground.png" alt="">
                </div>
                <div>
                    <img class="profile" src="profiles/garchomp.png" alt="">
                </div>
            </div>
            <div class="moves">
                <div class="icon"><img class="type" src="types/regular/rock.png" alt=""><p>Rock Slide</p></div>
                <div class="icon"><img class="type" src="types/regular/ground.png" alt=""><p>Earthquake</p></div>
                <div class="icon"><img class="type" src="types/regular/dragon.png" alt=""><p>Dragon Claw</p></div>
                <div class="icon"><img class="type" src="types/regular/normal.png" alt=""><p>Protect</p></div>
            </div>
        </div>
        `;
    }
}

customElements.define("pokemon-element", Pokemon)