// used to close notifications, modals, etc
const deleteParentBox = (evt) => {
  const notificationsBox = event.target.parentNode;
  notificationsBox.parentNode.removeChild(notificationsBox);
};
