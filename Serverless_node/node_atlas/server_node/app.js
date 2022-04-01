'use strict';

module.exports.find= async (event, context) => {
  const response = {
    status: 'done',
  };

  try {
    const body = {
        event: JSON.stringify(event),
        context: JSON.stringify(context),
    }

    // console.log('event, context:', JSON.stringify(event), JSON.stringify(context))

    response.body = JSON.stringify({
      code: 0,
      message: 'SUCCESS',
      data: body,
    });
 
    return response;
  } catch (err) {
    response.body = JSON.stringify({
      code: err.code || 1000,
      message: err.message || '未知错误'
    });
 
    return response;
  }
};