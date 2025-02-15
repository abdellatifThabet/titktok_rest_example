import asyncio
import logging

from typing import Tuple, Dict
from TikTokApi import TikTokApi

from src.db_models import User
from src.utils.serializers import UserSchema
from flask_app import db



tiktok_api = TikTokApi()
# Configure logging
logging.basicConfig(level=logging.INFO)


async def fetch_tiktok_user(username):
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[None], num_sessions=1, sleep_after=3)
        user = api.user(username)
        user_data = await user.info()
        return user_data
    
def create_user(payload)-> Tuple[int, Dict]:
    
    username = payload['username']
    
    # add user existance in db
    usr = User.query.filter_by(username=username).first()
    if usr:
        return 409, "user already exists"
    
    # get user data using tiktok api
    try:
        #tiktok_user = asyncio.run(fetch_tiktok_user(username))
        #logging.info(f"TikTok User Info: {tiktok_user.as_dict}")  
         
        ## the missing part here is where we get data from tiktok_user
        ## and place it the new created user obkect!
        new_user = User(username = username)         
        db.session.add(new_user)
        db.session.commit()
        return 201, {"message": "user added"}
    except Exception as e :
        logging.error(f"Error fetching TikTok user: {e}", exc_info=True)
        return 500, e
    
    
def get_user(ref_user)-> Tuple[int, Dict]:
    
    if ref_user.isdigit():
        logging.info(f"ref: {ref_user}")
        usr = User.query.filter_by(id=int(ref_user)).first()
    else: 
        usr = User.query.filter_by(username=ref_user).first()
        
    if not usr:
        logging.info(f"not user")
        return 404, {"trace": "user not found"}
    
    serialized_user = UserSchema().dump(usr)
    return 200, serialized_user